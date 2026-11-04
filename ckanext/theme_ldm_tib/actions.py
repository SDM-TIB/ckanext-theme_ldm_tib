from ckan.authz import is_sysadmin
from ckan.common import _, config
import ckan.plugins.toolkit as toolkit

CONSENT_FIELDS = ('specialconditions', 'dataprotection')


def _consent_required(context):
    """Only enforce when the legal notices are enabled, as in the template."""
    if not toolkit.asbool(config.get('tibtheme.legal_notices_enabled', False)):
        return False
    # Internal callers (CLI, other plugins) and sysadmins are exempt.
    if context.get('ignore_auth'):
        return False
    return not is_sysadmin(context.get('user'))


@toolkit.chained_action
def user_create(original_action, context, data_dict):
    if _consent_required(context):
        missing = [f for f in CONSENT_FIELDS
                   if not toolkit.asbool(data_dict.get(f))]
        if missing:
            messages = {
                'specialconditions': _('The Special Conditions have to be accepted.'),
                'dataprotection': _('Data processing by TIB must be approved.'),
            }
            labels = {
                'specialconditions': _('Special Conditions'),
                'dataprotection': _('Data Protection'),
            }
            raise toolkit.ValidationError(
                {f: [messages[f]] for f in missing},
                error_summary={labels[f]: messages[f] for f in missing},
            )
    # The flags are not part of the user schema, so don't pass them on.
    data_dict = {k: v for k, v in data_dict.items() if k not in CONSENT_FIELDS}
    return original_action(context, data_dict)
