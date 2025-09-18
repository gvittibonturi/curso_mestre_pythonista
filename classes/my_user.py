import administrador

one_user = administrador.User('glauco', 'bonturi', '47', 'masculino') 
one_user.describe_user()
one_user.greet_user()


other_user = administrador.User('gabriel', 'bonturi', '21', 'masculino')
other_user.describe_user()
other_user.greet_user()

first_admin = administrador.Admin('glauco', 'bonturi', '47', 'masculino')
first_admin.privileges.show_privileges()
