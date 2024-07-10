document.addEventListener('DOMContentLoaded', function () {
    var quill = new Quill('#editor-container', {
        theme: 'snow',
        placeholder: 'Write your blog content here...',
        modules: {
            toolbar: [
                [{ 'header': [1, 2, false] }],
                ['bold', 'italic', 'underline'],
                ['image', 'link'],
                [{ 'list': 'ordered'}, { 'list': 'bullet' }]
            ]
        }  
    });

    var form = document.getElementById('blog-form');
    form.onsubmit = function () {
        // Populate hidden form input with the editor's content
        var content = document.querySelector('input[name=content]');
        content.value = quill.root.innerHTML;
    };
});
