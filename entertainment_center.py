import media
import fresh_tomatoes

jungle_cruise = media.Movie("Jungle Cruise",
			 			"Storyline.",
			 			"https://xl.movieposterdb.com/21_07/2020/870154/xl_870154_a81c4d7a.jpg",
			 			"https://youtu.be/f_HvoipFcA8")

avatar = media.Movie("Avatar",
					"A marine on an alien planet.",
					"https://xl.movieposterdb.com/09_12/2009/499549/xl_499549_23ca4c37.jpg",
					"https://youtu.be/MknKGdvuYKo")

red_notice = media.Movie("Red Notice",
					"Storyline.",
					"https://xl.movieposterdb.com/21_11/2021/7991608/xl_7991608_44a01457.jpg?v=2021-11-11%2022:43:14",
					"https://youtu.be/Pj0wz7zu3Ms")

no_way_home = media.Movie("Spider man - No way home",
					"Storyline.",
					"https://xl.movieposterdb.com/21_11/2021/10872600/xl_10872600_b0b5d3cc.jpg",
					"https://youtu.be/JfVOs4VSpmA")

the_batman = media.Movie("The Batman",
					"Storyline.",
					"https://xl.movieposterdb.com/21_12/2020/11373302/xl_11373302_a1b18b7a.jpg",
					"https://youtu.be/mqqft2x_Aa4")

hunger_games = media.Movie("Hunger games",
					"Storyline.",
					"https://xl.movieposterdb.com/12_02/2012/1392170/xl_1392170_7bed9f27.jpg",
					"https://youtu.be/mfmrPu43DF8")

movies = [jungle_cruise,avatar,red_notice,no_way_home,the_batman,hunger_games]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
