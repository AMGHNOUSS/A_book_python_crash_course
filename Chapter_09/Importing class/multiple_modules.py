from privileges import Admin

admin = Admin('Redouane', 'AMGHNOUSS', 21, 'Laayoune')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()