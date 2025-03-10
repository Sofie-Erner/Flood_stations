//const d = new Date();

txt = d.getHours() + ":";

const min = d.getMinutes()

if (min < 10){
	txt = txt + "0" + min;
}
else {
	txt = txt + min;
}

const date = [d.getDate(),d.getMonth()];
txt = txt  + "     ";

for (let x in date) {
  if (date[x] < 10){
	txt = txt + "0" + date[x] + "/";
  }
  else {
     txt = txt + date[x] + "/";
  }
}

txt = txt + d.getFullYear();

document.getElementById("datetime").innerHTML = txt;