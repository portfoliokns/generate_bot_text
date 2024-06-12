<html>
<body>
<h1>bot文章生成アプリ</h1>
<form method="post" action="/" enctype="multipart/form-data">
<textarea id="textarea" name="input_text" rows="4" cols="50">{{input_text}}</textarea><br>
<input type="button" value="テキスト削除" onclick="clearTextarea()">
<input type="submit" value="生成">
</form>
<ul>
<li>{{!output_text[0]}}</li>
<li>{{!output_text[1]}}</li>
<li>{{!output_text[2]}}</li>
<li>{{!output_text[3]}}</li>
<li>{{!output_text[4]}}</li>
</ul>
<script>
function clearTextarea() {
  document.getElementById('textarea').value = '';
};
</script>
</body>
</html>

