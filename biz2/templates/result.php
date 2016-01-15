<html>
<?php echo "hi" ?>
	<head></head>
	<body>
		<form action="." method="POST">
			{% csrf_token %}
			<input type="text" name="num1">
			<input type="text" name="num2">
			<input type="submit" value="add">
		</form>
		{% if result %}
		<div class="res">The result is: {{ result }}</div>
		{% endif %}
	</body>
</html>