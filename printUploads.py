#!/usr/bin/env python3

import json, requests, re

debug = False

port = 9092
user = 'test'
pw = 'tset'

def debugDump(label, data):
	if not debug: return
	print(label, json.dumps(data, sort_keys=True, indent=4))

def sendRequest(function, data = None):
	url = 'http://127.0.0.1:' + str(port) + function

	debugDump('POST: ' + url, data)
	resp = requests.post(url=url, json=data, auth=(user, pw))

	# gracefully add 401 error
	if resp.status_code == 401:
		return {'retval': False}

	debugDump('RESP', resp.json())
	return resp.json()
	
	
if __name__ == "__main__":
	files = sendRequest('/RsFiles/FileUploads')['hashs']
	
	for file in files:
		print(hash)
		req = {'hash': file}
		details = sendRequest('/RsFiles/FileDetails', req)['info']
		print(info)
		print(hintflags)
