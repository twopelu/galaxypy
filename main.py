import galaxy

print("GALAXY Big Bang!")
bookmarks = galaxy.read_bookmarks('test/bookmarks_31_3_21.html')
galaxy.build_galaxy(bookmarks)
print("GALAXY Big Crunch!")
