// const venn2 = document.getElementById("venn2");

function canShadeVenn(vennid) {
  const venn = document.getElementById(vennid);

  const twoset = document.getElementById("AB");
  twoset.addEventListener("click", function (event) {
    var classes = twoset.classList;
    var classesList = Array.from([...classes]);
    console.log("ABSs");
    if (classesList.includes("active")) {
      twoset.classList.remove("active");
    } else {
      twoset.classList.add("active");
    }
  });
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
    const matchingElems = document.querySelectorAll("." + svgId);

    var classes = event.target.classList;
    var classesList = Array.from([...classes]);
    if (classesList.includes("active")) {
      event.target.classList.remove("active");
    } else {
      event.target.classList.add("active");
    }

    // if (svgId == "ABC" || svgId == "AC") {
    //   console.log("spedialcase");
    //   const svgId2 = svgId == "ABC" ? "AC" : "ABC";
    //   const matchingElems = document.querySelectorAll("." + svgId2);
    //   console.log(matchingElems);

    //   var classes = event.target.classList;
    //   var classesList = Array.from([...classes]);
    //   event.target.classList.add("active");
    // }

    // matchingElems.forEach(function (elem) {
    //   if (elem.className == "active") {
    //     elem.classList.remove("active");
    //   } else {
    //     elem.classList.add("active");
    //   }
    // });

    // Add active class to clicked element
  });
  // venn2.addEventListener("click", function (event) {
  //   // Remove active class from all paths
  //   //   const paths = this.querySelectorAll('path');
  //   //   paths.forEach(function(path) {
  //   //     path.classList.remove('active');
  //   //   });
  //   // const paths = this.querySelectorAll("path");
  //   // paths.forEach(function (path) {
  //   //   path.classList.remove("highlight");
  //   // });
  //   // Add active class to matching elements
  //   const svgId = event.target.getAttribute("id");
  //   console.log(svgId);
  //   const matchingElems = document.querySelectorAll("." + svgId);

  //   var classes = event.target.classList;
  //   var classesList = Array.from([...classes]);
  //   if (classesList.includes("active")) {
  //     event.target.classList.remove("active");
  //   } else {
  //     event.target.classList.add("active");
  //   }

  //   // if (svgId == "ABC" || svgId == "AC") {
  //   //   console.log("spedialcase");
  //   //   const svgId2 = svgId == "ABC" ? "AC" : "ABC";
  //   //   const matchingElems = document.querySelectorAll("." + svgId2);
  //   //   console.log(matchingElems);

  //   //   var classes = event.target.classList;
  //   //   var classesList = Array.from([...classes]);
  //   //   event.target.classList.add("active");
  //   // }

  //   // matchingElems.forEach(function (elem) {
  //   //   if (elem.className == "active") {
  //   //     elem.classList.remove("active");
  //   //   } else {
  //   //     elem.classList.add("active");
  //   //   }
  //   // });

  //   // Add active class to clicked element
  // });
}

// venn.addEventListener("mouseover", function (event) {
//   const paths = this.querySelectorAll("path");
//   paths.forEach(function (path) {
//     path.classList.remove("highlight");
//   });

//   // Add active class to matching elements
//   const svgId = event.target.getAttribute("id");
//   const matchingElems = document.querySelectorAll("." + svgId);

//   var classes = event.target.classList;
//   var classesList = Array.from([...classes]);
//   if (classesList.includes("highlight")) {
//     event.target.classList.remove("highlight");
//   } else {
//     event.target.classList.add("highlight");
//   }
// });

function getRegions() {
  const active = document.getElementsByClassName("active");
  const activeList = [];
  for (i in active) {
    if (active[i].id) {
      if (active[i].id == "venn2" || active[i].id == "venn3") {
        activeList.push("");
      } else {
        activeList.push(active[i].id);
      }
    }
  }
  if (activeList.length == 0) {
    return {};
  }
  return "{'" + activeList.join("','") + "'}";
}

function shadeRegions(set) {
  const paths = document.querySelectorAll("path");
  paths.forEach(function (path) {
    path.classList.remove("active");
  });

  const regionsList = set
    .replace("{", "")
    .replace("}", "")
    .replaceAll("&#x27;", "")
    .split(",");

  for (i in regionsList) {
    const matchingElems = document.getElementById(regionsList[i]);
    matchingElems.classList.add("active");
  }
}
