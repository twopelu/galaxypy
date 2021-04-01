import galaxy

print("GALAXY Big Bang!")
bookmarks = galaxy.read_bookmarks('/home/dani/Documentos/bookmarks_31_3_21.html')
galaxy.build_galaxy(bookmarks, ['angular', 'javascript'])
print("GALAXY Big Crunch!")
