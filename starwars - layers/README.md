# My Flask App

Run project with `makefile`

    make build

And run Docker image with `makefile`
    
    make run

You need to have Docker up for this to work.

# Project requirements

1. Endpoint `GET /` list the Star wars movies.
   * Sort them by ID in ascending order.

2. Create a new Endpoint to list all character names from a movie.
   * You pass an ID as a URL parameter. 