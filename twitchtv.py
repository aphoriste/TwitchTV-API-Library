"""
TwitchTV API Library by aphoriste
License: GPLv3
"""

import requests
import simplejson as json


class api:
	def __init__(self):
		self.token = 'Unauthenticated'
		self.header()
		return

	def header(self):
		return {'Authorization' : 'OAuth %s' % self.token}

	def implicit_grant_flow(self, client_id, redirect_uri, scope, token=''):
		"""
		Function for implicit grant flow authorization.
		"""
		if token == '':
			self.token = raw_input('Go to %s - after signing in it will redirect you, copy and paste access_token from your browser here: ' % ('https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=%s&redirect_uri=%s&scope=%s' % (client_id, redirect_uri, scope)))
		else:
			self.token = code
		return True

	def authorization_code_flow(self, client_id, client_secret, scope, redirect_uri, code=''):
		"""
		Function for authorization code flow authorization.
		"""
		if code == ''
			code = raw_input('Go to %s - after signing in it will redirect you, copy and paste ?code=<code> here: ' % ('https://api.twitch.tv/kraken/oauth2/authorize?response_type=code&client_id=%s&redirect_uri=%s&scope=%s' % (client_id, redirect_uri, scope) ))
		
		payload = {

		'client_id': client_id,
		'client_secret': client_secret,
		'grant_type': 'authorization_code',
		'redirect_uri': redirect_uri,
		'code': code

		}
		self.token = json.loads(requests.post('https://api.twitch.tv/kraken/oauth2/token', params=payload).text)['access_token']
		return True

	def password_creditional_grant_flow(self, client_id, client_secret, scope, username, password):
		"""
		Function for password creditional grant flow.
		A TwitchTV admin must grant you access to this.
		"""
		payload = {

		'grant_type': 'password',
		'client_id': client_id,
		'client_secret': client_secret,
		'username': username,
		'password': password,
		'scope': scope

		}
		self.token = json.loads(requests.post('https://api.twitch.tv/kraken/oauth2/token', params=payload).text)['access_token']
		return True

	def users_login_blocks(self, login,  method, target='', limit='', offset=''):
		"""
		Initial function for /users/:login/blocks
		"""
		method = method.lower()
		payload = {}
			
		if limit != '' or offset != '':
			if limit != '':
				payload['limit'] = limit
			if offset != '':
				payload['offset'] = offset
		if 'get' in method:
			return self.get_login_blocks(login, payload)
		
		elif 'put' in method:
			return self.put_login_blocks(login, target, payload)
		
		elif 'delete' in method:
			return self.delete_login_blocks(login, target, payload)
		
		else:
			return False

	def get_login_blocks(self, login, payload={}):
		"""
		GET request
		"""
		return requests.get('https://api.twitch.tv/kraken/users/%s/blocks' % login, params=payload, headers=self.header())

	def put_login_blocks(self, login, target, payload={}):
		"""
		PUT request
		"""
		return requests.put('https://api.twitch.tv/kraken/users/%s/blocks/%s' % (login, target), params=payload, headers=self.header())

	def delete_login_blocks(self, login, target, payload={}):
		"""
		DELETE request
		"""
		return requests.delete('https://api.twitch.tv/kraken/users/%s/blocks/%s' % (login, target), params=payload, headers=self.header())

	def channels_channel(self, user):
		"""
		GET request
		"""
		return requests.get('https://api.twitch.tv/kraken/channels/%s' % user)

	def channel(self):
		"""
		GET request
		"""
		return requests.get('https://api.twitch.tv/kraken/channel', headers=self.header())

	def channels_channel_editors(self, user):
		"""
		GET request
		"""
		return requests.get('https://api.twitch.tv/kraken/channels/%s/editors' % user, headers=self.header())

	def put_channels_channel(self, user, status='', game='', payload={}):
		"""
		PUT request
		"""
		if status != '' or game != '':
			if status != '':
				payload['status'] = status

			if game != '':
				payload['game'] = game

		return requests.put('https://api.twitch.tv/kraken/channels/%s'% user, params=payload, headers=self.header())

	def channels_channel_videos(self, user, limit='', offset='', broadcasts=False, payload={}):
		"""
		GET request
		"""
		if limit != '':
			payload['limit'] = limit

		if offset != '':
			payload['offset'] = offset

		if broadcasts != False:
			payload['broadcasts'] = broadcasts

		return requests.get('https://api.twitch.tv/kraken/channels/%s/videos'% user, params=payload, headers=self.header())

	def channels_channel_follows(self, user, limit='', offset='', payload={}):
		"""
		GET request
		"""
		if limit != '':
			payload['limit'] = limit

		if offset != '':
			payload['offset'] = offset

		return requests.get('https://api.twitch.tv/kraken/channels/%s/follows' % user, params=payload)

	def channels_channel_streamkey(self. user):
		"""
		DELETE Request
		"""
		return requests.delete('https://api.twitch.tv/kraken/channels/%s/stream_key' % user, headers=self.header())

	def channels_channel_commercial(self, user, length='', payload={}):
		"""
		POST Request
		"""
		if length != '':
			payload['length'] = length

		return requests.post('https://api.twitch.tv/kraken/channels/%s/commercial' % user, params=payload, headers=self.header())

