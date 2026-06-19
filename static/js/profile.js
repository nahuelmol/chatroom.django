
document.getElementById('follower_show').addEventListener('click', function() {
    var section = document.getElementById('follower_section');
    section.style.display = (section.style.display === 'none' || section.style.display === '') ? 'block' : 'none';
});

document.getElementById('following_show').addEventListener('click', function() {
    var section = document.getElementById('following_section');
    section.style.display = (section.style.display === 'none' || section.style.display === '') ? 'block' : 'none';
});

document.getElementById('chatroom_show').addEventListener('click', function(){
    var section = document.getElementById('chatroom_section');
    section.style.display = (section.style.display === 'none' || section.style.display === '') ? 'block' : 'none';
});
