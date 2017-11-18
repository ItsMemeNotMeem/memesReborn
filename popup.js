$(document).ready(function(){
  const memeUrl = 'https://api.imgflip.com/get_memes'
  function getMemes(){
    return new Promise(function(resolve, reject){
      fetch(memeUrl)
      .then(response=>response.json())
      .then(data=>{console.log(data); resolve(data)})
    })
  }

  (function getUrl(callback){
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
      url = tabs[0].url;
      callback(url)
    });
  })(console.log)
  console.log('memes')
  var $divParent = $('<div>')
  $divParent.addClass('parent')
  getMemes().then(function(data){
    console.log('data', data)
    var memes = data.data.memes
    for(var i = 0; i < 12; i++){
      $divChild= $('<div>')
      $p = $('<p>')
      memes[i]
      var name = memes[i].name
      var url = memes[i].url
      var width = memes[i].width
      var height = memes[i].height
      console.log('name url width height', name, url, width, height)
      $p.text(name)
      var $img = $('<img>')    
      $img.attr({name:name, src: url, width: 250})
      $divChild.append($p)
      $divChild.append($img)
      $divParent.append($divChild)
    }
    $('#memes').append($divParent)
  })


})



