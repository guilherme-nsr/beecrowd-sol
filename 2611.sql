/* psql 9.4.19 */

SELECT movies.id, movies.name FROM movies JOIN genres ON genres.id = movies.id_genres WHERE genres.description = 'Action';