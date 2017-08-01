function Task1Done(dope)
{
	var bulletstyle = document.getElementById(dope).style.textDecoration;
  if ( bulletstyle== 'line-through' )
  		document.getElementById(dope).style.textDecoration='none';
 	else
 			 document.getElementById(dope).style.textDecoration='line-through';


}
