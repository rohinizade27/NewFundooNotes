   $(document).ready(function () {

      $('#update-content').click(function () {
                $('#modal-title').val($('#title').text());
                $('#modal-description').val($('#description').text());

                // get the src of the image
                var image_src = $("#note-img").attr('src');

                // assign it to the modal's body
                $("#modal-img").attr('src',image_src);

            });



      $('#update-img').click(function () {
            $('#modal-title').val($('#title').text());
            $('#modal-description').val($('#description').text());

            // get the src of the image
            var image_src = $("#note-img").attr('src');

            // assign it to the modal's body
            $("#modal-img").attr('src',image_src);

        });




        });


