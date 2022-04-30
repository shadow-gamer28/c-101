import dropbox

class TransferData :
    def __init__(self, access_token) :
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to) :
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGgjWKhIDUNcPfEyET3tjKGRHsZ-l9IoajoB8vfkJ5147FXEG4VewOMTm4R3oAOP1AhLoNkZ1MWj4xj8Xdc0qmCslCUIHBVyFDNZvLOc4LnMvGtuzWSz0ddYgL_UQnX67MLOCxM'
    transferData = TransferData(access_token)
    file_from = input("Enter the file address that has to be transfered: ")
    file_to = input("Enter the address to upload in tha dropbox: ")
    transferData.upload_file(file_from, file_to)
    print("Your file has been transferred!!")

main()