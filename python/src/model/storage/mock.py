# import pyrebase
#
#
# config= {
#     "apiKey": "apiKey",
#     "authDomain": "projectId.firebaseapp.com",
#     "databaseURL": "https://memesearch-1010.firebaseio.com/",
#     "storageBucket": "projectId.appspot.com"
# }
#
# firebase = firebase.FirebaseApplication("https://memesearch-1010.firebaseio.com")
# result = firebase.get("/AllMemes", None)
# print(result)

#
# firebase = pyrebase.initialize_app(config)
#
# #auth
# auth = firebase.auth()
# uid = 'rick-and-morty-memes-uid'
# additional_claims = {
#     'premiumAccount': True
# }
# custom_token = auth.create_custom_token(uid, additional_claims)
# user = auth.sign_in_with_custom_token(custom_token)
#
# #db
# db = firebase.database()
# data = {
#     "name": "Mortimer 'Morty' Smith"
# }
# results = db.child("users").push(data, user['idToken'])
