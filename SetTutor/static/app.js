const venn = document.getElementById("venn");

venn.addEventListener("click", function (event) {
  // Remove active class from all paths
  //   const paths = this.querySelectorAll('path');
  //   paths.forEach(function(path) {
  //     path.classList.remove('active');
  //   });
  // const paths = this.querySelectorAll("path");
  // paths.forEach(function (path) {
  //   path.classList.remove("highlight");
  // });
  // Add active class to matching elements
  const svgId = event.target.getAttribute("id");
  console.log(svgId);
  // console.log("svgid", svgId);
  const matchingElems = document.querySelectorAll("." + svgId);
  // console.log("mathcingelems", matchingElems);
  // console.log(event.target.classList[0] == "active");

  var classes = event.target.classList;
  var classesList = Array.from([...classes]);
  if (classesList.includes("active")) {
    event.target.classList.remove("active");
  } else {
    event.target.classList.add("active");
  }

  // matchingElems.forEach(function (elem) {
  //   if (elem.className == "active") {
  //     elem.classList.remove("active");
  //   } else {
  //     elem.classList.add("active");
  //   }
  // });

  // Add active class to clicked element
});

venn.addEventListener("mouseover", function (event) {
  const paths = this.querySelectorAll("path");
  paths.forEach(function (path) {
    path.classList.remove("highlight");
  });

  // Add active class to matching elements
  const svgId = event.target.getAttribute("id");
  // console.log("svgid", svgId);
  const matchingElems = document.querySelectorAll("." + svgId);
  // console.log("mathcingelems", matchingElems);
  // console.log(event.target.classList[0] == "highlight");

  var classes = event.target.classList;
  var classesList = Array.from([...classes]);
  if (classesList.includes("highlight")) {
    event.target.classList.remove("highlight");
  } else {
    event.target.classList.add("highlight");
  }
});

function getRegions() {
  console.log("GET REGIONS");
  const active = document.getElementsByClassName("active");
  const activeList = [];
  for (i in active) {
    if (active[i].id) {
      activeList.push(active[i].id);
    }
  }
  console.log(activeList);
  const regionsList = document.getElementById("regions-list");
  regionsList.innerHTML = activeList;
}
