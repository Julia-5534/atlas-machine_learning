-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genre, COUNT(show_id) AS number_of_shows
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
GROUP BY genre
HAVING COUNT(show_id) > 0
ORDER BY number_of_shows DESC;
