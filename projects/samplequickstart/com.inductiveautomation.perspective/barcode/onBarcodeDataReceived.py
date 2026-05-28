def onBarcodeDataReceived(session, data, context):
	session.custom.device.barcode = data