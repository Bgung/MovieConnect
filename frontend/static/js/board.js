document.querySelector("button[type='submit']").addEventListener("click", () => {
    const title = document.querySelector("input[name='title']").value;
    const content = document.querySelector("textarea[name='content']").value;
    const author = document.querySelector("input[name='author']").value;

    if (title === "" || content === "" || author === "") {
        alert("Please fill in all fields.");
        return;
    }

    fetch("/board/new_post", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title,
            content,
            author,
        }),
    })
        .then((response) => {
            response.json();
        })
        .then((data) => {
            if (data.status_code === 201) {
                alert("Successfully posted.");
                location.href = "/boards";
            } else {
                alert("Failed to post.");
            }
        });
});
