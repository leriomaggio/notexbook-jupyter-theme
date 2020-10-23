/*
Author: Valerio Maggio (@leriomaggio)
http://github.com/leriomaggio

 ==================================================
 Custom JQuery function that handles the scrolling
 to anchor links positioning the landing of the top
 pixel to the correct offset, considering that the
 header toolbar is FIXED by default.
 ==================================================

*/

function customise_anchor_links_click() {
    $("a").on("click", function (e) {
        // Check if header toolbar is visible in the first place
        if (this.hash !== "") {
            // Remove any existing handler
            $(this).unbind();
            // Store hash
            const hash = this.hash;
            let t = $(hash);
            if ((t === undefined) || (t.length === 0)) {
                let anchor = hash.substr(1);
                t = $("a[name='" + anchor + "'");
            }
            if ((t !== undefined) && (t.length > 0)) {
                // Prevent default anchor click behavior
                e.preventDefault();
                // Using jQuery's animate() method to add smooth page scroll
                // The optional number (800) specifies the number of milliseconds
                // it takes to scroll to the specified area
                let header_height = $("#header").height();
                let offset = $(t).offset().top - header_height;
                $('html, body').animate({
                    scrollTop: offset
                }, 800, function () {});
            }
            // console.log(hash);
            // console.log(t);
        }
    });
}

// Trigger the selection when the page is ready
$(document).ready(function () {
    customise_anchor_links_click();
});

/*
 Trigger a new selection scan every time a
 Markdown cell is rendered -
 so that (possible) newly defined links can be captured.
 */
$([IPython.events]).on("rendered.MarkdownCell", function () {
    customise_anchor_links_click();
});