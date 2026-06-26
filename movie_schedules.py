
current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}

print("We're showing the following movies:")
for key in current_movies:
      print(key)
      #movie = input("What movie would you like the showtime for?\n")     
movie = input("What movie would you like the showtime for?\n")
      
showtime = current_movies.get(movie)
if showtime == None:
      print("Requested movie isn't playing")
else:
      #print(current_movies.get(movie[0]))
      print(movie, 'is playing at', showtime)
      
#print('The Grinch' == ' The Grinch')
      
 current_movies.describe()
 current_movies.head
  current_movies.info
  
      