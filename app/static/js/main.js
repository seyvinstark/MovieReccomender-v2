//this says that everytime we submit a form it takes whats in the form and put it the getmovie function
/*$(document).ready(
()=> {
    $('#searchForm').on('submit',(e)=>{
        let searchText = $('#searchText').val();

        getMovies(searchText);
        //getPoster();
        e.preventDefault();
    });
}
*/
//getMovie());

//get movies function
function getMovies(searchText){
    axios.get('http://www.omdbapi.com?apiKey=fb6fa5d1'+'&s='+searchText)
        .then((response)=>{
            console.log(response);
            let movies = response.data.Search;
            let output='';
            //loop to put the whole thing in an array
            $.each(movies,(index,movie)=>{
                output += `
                <div class="col-md-3">
                    <div class="well text-center">
                        <img src="${movie.Poster}">
                        <h5>${movie.title}</h5>
                        <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary" href="#">Movie Details</a>
                    </div>    
                </div>
                `;
            });
            $('#movies').html(output);
        })
        .catch((err)=>{
            console.log(err);
        });

}

//when we select a movie
function movieSelected(id){
    //it takes our movie id and stores in session so we can use it in other pages
    sessionStorage.setItem('movieId', id);
    //window.location = 'movie.html';
    return false;
}
function getImagepost() {

}

    document.querySelectorAll(".imagePost").forEach(function (element) {
    var link = element.getAttribute("data-link");
    console.log(link);
    element.addEventListener('load', function (e) {
        axios.get(link).then((response)=>{
            let img = response.data.Poster;
            console.log(img);
            element.setAttribute("src",img );
        }) .catch((err)=>{
            console.log(err);
        });


    })
})
function getPoster(e){
    let movieId = sessionStorage.getItem('movieId');
    axios.get('http://www.omdbapi.com?apiKey=fb6fa5d1'+'&i='+movieId)
        .then((response)=>{
            console.log(response);
            let movie = response.data;
            let imgoutput=`
                <img src="${movie.Poster}" class="img-responsive"/>
            `;
            $("#movieposter").html(imgoutput)
        })
        .catch((err)=>{
            console.log(err);
        });
}

//get movie function
function getMovie(){
    let movieId = sessionStorage.getItem('movieId');

     axios.get('http://www.omdbapi.com?apiKey=fb6fa5d1'+'&i='+movieId)
        .then((response)=>{
            console.log(response);
            let movie = response.data;

            let output=`
                <div class="row">
                    <div class="col-md-4">
                        <img src="#{movie.Poster}" class="thumbnail">
                    </div>
                    <div class="col-md-8">
                        <h2>${movie.Title}</h2>
                        <ul class="list-group">
                            <li class="list-group-item"> <strong>Genre:</strong> ${movie.Genre}</li>
                            <li class="list-group-item"> <strong>Released:</strong> ${movie.Released}</li>
                            <li class="list-group-item"> <strong>rated:</strong> ${movie.Rated}</li>
                            <li class="list-group-item"> <strong>IMDB ratings</strong>:</strong> ${movie.imdbRating}</li>
                            <li class="list-group-item"> <strong>Director:</strong> ${movie.Director}</li>
                            <li class="list-group-item"> <strong>Writer:</strong> ${movie.Writer}</li>
                            <li class="list-group-item"> <strong>Actors :</strong> ${movie.Actors}</li>
                        </ul>
                    </div>
                </div>
                <div class="row">
                    <div class="well">
                        <h3>Plot</h3>
                        ${movie.Plot}
                        <hr>
                        <a href="http://imdb.com/title/${movie.imdbID}" target="_blank" class="btn btn-primary" >View imdb</a>
                        <a href="home.html" class="btn btn-default">go back to search</a>
                    </div>
                </div>
            `;
            $('#movie_results').html(output);

        })
        .catch((err)=>{
            console.log(err);
        });
}

