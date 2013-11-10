import twitchtv
import simplejson as json

api = twitchtv.api()

api.implicit_grant_flow('jdlgprcb74o1ym5xvreiyfuz0znhvci', 'http://localhost/', 'user_blocks_edit')
print json.loads(api.users_login_blocks('obnoxioustheegod', 'PUT', 'Quelvera').text)