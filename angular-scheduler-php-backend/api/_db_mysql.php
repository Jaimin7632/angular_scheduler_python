<?php
$host = "127.0.0.1";
$port = 3306;
$username = "username";
$password = "password";
$database = "angular-scheduler";

$db = new PDO("mysql:host=$host;port=$port",
               $username,
               $password);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$db->exec("CREATE DATABASE IF NOT EXISTS `$database`");
$db->exec("use `$database`");

function tableExists($dbh, $id)
{
    $results = $dbh->query("SHOW TABLES LIKE '$id'");
    if(!$results) {
        return false;
    }
    if($results->rowCount() > 0) {
        return true;
    }
    return false;
}

$exists = tableExists($db, "events");

if (!$exists) {
    //create the database
    $db->exec("CREATE TABLE events (
        id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name TEXT,
        start DATETIME,
        end DATETIME,
        resource_id VARCHAR(30))");

    $db->exec("CREATE TABLE groups (
        id INTEGER  NOT NULL PRIMARY KEY,
        name VARCHAR(200)  NULL)");

    $db->exec("CREATE TABLE resources (
        id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(200)  NULL,
        group_id INTEGER  NULL)");

    $items = array(
        array('id' => '1', 'name' => 'People'),
        array('id' => '2', 'name' => 'Tools'),
    );
    $insert = "INSERT INTO groups (id, name) VALUES (:id, :name)";
    $stmt = $db->prepare($insert);
    $stmt->bindParam(':id', $id);
    $stmt->bindParam(':name', $name);
    foreach ($items as $m) {
      $id = $m['id'];
      $name = $m['name'];
      $stmt->execute();
    }

    $items = array(
        array('group_id' => '1', 'name' => 'Person 1'),
        array('group_id' => '1', 'name' => 'Person 2'),
        array('group_id' => '1', 'name' => 'Person 3'),
        array('group_id' => '2', 'name' => 'Tool 1'),
        array('group_id' => '2', 'name' => 'Tool 2'),
        array('group_id' => '2', 'name' => 'Tool 3'),
    );
    $insert = "INSERT INTO resources (group_id, name) VALUES (:group_id, :name)";
    $stmt = $db->prepare($insert);
    $stmt->bindParam(':group_id', $group_id);
    $stmt->bindParam(':name', $name);
    foreach ($items as $m) {
      $group_id = $m['group_id'];
      $name = $m['name'];
      $stmt->execute();
    }

}
