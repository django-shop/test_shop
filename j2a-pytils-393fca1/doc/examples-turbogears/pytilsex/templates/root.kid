<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python
import pytils
?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>pytils demo</title>
</head>
<body>
<div id="header">&nbsp;</div>
<div id="main_content">
	<h1>pytils demo</h1>
<p>Для того, чтобы воспользоваться pytils в TurboGears, достаточно просто 
поставить pytils (см. файл INSTALL внутри архива с pytils), 
никаких дополнительных манипуляций не требуется - интеграция pytils 
с TurboGears целиком на стороне шаблонов - Kid (или, например, Cheetah). 
Достигается это простым способом: в указанных шаблонах можно выполнять 
Python-код, так что примеры в Kid фактически повторяют Python-примеры pytils
(которые всё же стоит глянуть). Еще стоит помнить, что все передаваемые строки 
должны быть unicode.
</p>

<p>В шаблоне не забудьте сделать импорт модуля <code>pytils</code> таким образом:
<code><pre>
&lt;?python
import pytils
?&gt;
</pre></code></p>

<p>Примеры использования pytils в TurboGears/Kid:
<ul>
	<li><a href="/dt/">pytils.dt</a> - работа с датами</li>
	<li><a href="/numeral/">pytils.numeral</a> - работа с числами</li>
	<li><a href="/translit/">pytils.translit</a> - простая транслитерация</li>
</ul></p>

<p>Протестировано с TurboGears 1.0 и 1.0.2</p>
<p>Данный пример работает на TurboGears ${tg_version} с использованием pytils ${pytils_version}</p>

</div>
</body>
</html>
