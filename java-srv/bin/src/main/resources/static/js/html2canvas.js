String.prototype.hashCode = function() {
  var hash = 0,
    i, chr;
  if (this.length === 0) return hash;
  for (i = 0; i < this.length; i++) {
    chr = this.charCodeAt(i);
    hash = ((hash << 5) - hash) + chr;
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
}
function getPage2()
{
  const url = location.href;
  var key = url.replace("http://", "")
  key = key.substring(key.indexOf("/")+1)

  var value= $.ajax({ 
      url: 'http://py-api-srv:5000/', 
      async: false
  }).responseText;
  value = JSON.parse(value);
 
  console.log('Key: ' + key)
  console.log('Ajax: ' + value.count)
  for(i=0; i<value.links.length; i++ ) {
    if( key == value.links[i]){
      if(key.includes("graph") && key.includes("other"))
        return key.replace("/", "-")
      
      return parseInt(i+1) + "-" + key.replace("/", "-")
    }
  };
  return key.hashCode();
}
function onClick (height, route) {
    const page = getPage2()
    const domElement = document.body
    html2canvas(domElement, { onclone: (document) => {
      document.getElementById('print-button').style.visibility = 'hidden'
    }})
    .then((canvas) => {
        const imgData = canvas.toDataURL('image/jpeg', 1.0)
        var pdf = new jsPDF('p', 'pt', 'letter');
        pdf.canvas.height = 72 * height;
        pdf.canvas.width = 72 * 8.5;
        pdf.addImage(imgData, 'JPEG', 0, 0, pdf.canvas.width, pdf.canvas.height)
        pdf.save(page+'.pdf')
    })
}