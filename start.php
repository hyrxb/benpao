<?php

require_once __DIR__ . '/Workerman/Autoloader.php';
use Workerman\Worker;

// 运行在主进程
$tcp_worker = new Worker("tcp://0.0.0.0:2347");
// 赋值过程运行在主进程
$tcp_worker->onMessage = function($connection, $data)
{
    // 这部分运行在子进程
    $connection->send('hello ' . $data);
};
// var_dump($argv);
Worker::runAll();
