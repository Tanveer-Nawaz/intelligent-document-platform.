document.getElementById("uploadForm").onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
};
