// $(document).on('click', '.pagination-button', function () {

// $('.pagination-butto').on('click', function () {
//     var currentPage = $(this).data('page');
//     var href = $(this).attr("href");

//     console.log(currentPage);
//     console.log(href);
//     // $.ajax({
//     //     url: '/update_jobs',
//     //     type: 'POST',
//     //     data: {'currentPage': currentPage},
//     //     success: function(data) {
//     //         // update currentPage variable in your Flask app
//     //         currentPage = data.currentPage
//     //         // re-render the template with new data
//     //         renderJobs(data.job_listings);
//     //     }
//     // });
// });

// log('loaded')
console.log('loaded');
const paginationLinks = document.querySelectorAll('.pagination-button');

paginationLinks.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        console.log('selected clicked');
    });
});