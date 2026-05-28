def onNdefDataReceived(session, data, context):
	session.custom.device.nfc = data