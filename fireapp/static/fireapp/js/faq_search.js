const user_input = $('#hero-input-area') //search bar
const search_submit = $('#hero-form') //search bar form submit
const questions_div = $('#replaceable-content') // div containing the questions
const endpoint = '/faq/' // url to the faq page
const delay_by_in_ms = 700
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the questions_div, then:
            questions_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                questions_div.html(response['html_from_view'])
                // fade in the div with new contentss
                questions_div.fadeTo('slow', 1)
            })
        })
};


// submit search on typing
user_input.on('keyup', function () {

    const request_parameters = {
        q: $(this).val() // value of the search bar
    }

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the id of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
});

// removes functionality to the submit button
search_submit.submit(function (event) {

    event.preventDefault() // cancel the html form submition
});