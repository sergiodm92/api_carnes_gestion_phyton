

def custom_Response_Exito(data):
    return {
        "status": "ok",
        "status_code": 200,
        "data": data
    }

def custom_Response_Error(message, status_code):
    return {
        "status": "error",
        "status_code": status_code,
        "message": message
    }


