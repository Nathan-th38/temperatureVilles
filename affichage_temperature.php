<?php

$bdd = new PDO('mysql:host=localhost;dbname=bdd_temperaturevilles;charset=utf8', 'root', '');
$bdd->query("set lc_time_names ='fr_FR'");

$reponse = $bdd->prepare("SELECT temperature,DATE_FORMAT(last_update, '%d %M %Y à %Hh%i') AS date FROM temperaturevilles WHERE ville = ?");
$reponse->execute(array($_GET['ville']));

while ($donnees = $reponse->fetch())
{
    echo ('Le '.$donnees['date'].' il faisait '.$donnees['temperature'].'°C à '.htmlspecialchars(ucfirst($_GET['ville'])));
}

$reponse->closeCursor();

?>