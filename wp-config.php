<?php

/**

 * The base configuration for WordPress

 *

 * The wp-config.php creation script uses this file during the installation.

 *

 * @package WordPress

 */

// 1. Ép nhận diện HTTPS từ Ngrok để tránh vòng lặp 302

if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {

    $_SERVER['HTTPS'] = 'on';

}



// 2. Tự động cấu hình URL theo link Ngrok hiện tại

if (isset($_SERVER['HTTP_HOST'])) {

    define('WP_HOME', 'https://' . $_SERVER['HTTP_HOST'] . '/wordpress');

    define('WP_SITEURL', 'https://' . $_SERVER['HTTP_HOST'] . '/wordpress');

}

// ** Database settings - You can get this info from your web host ** //

define( 'DB_NAME', 'wordpress' );

define( 'DB_USER', 'root' );

define( 'DB_PASSWORD', '' );

define( 'DB_HOST', 'localhost' );

define( 'DB_CHARSET', 'utf8mb4' );

define( 'DB_COLLATE', '' );



/**#@+

 * Authentication unique keys and salts.

 */

define( 'AUTH_KEY',         'put your unique phrase here' );

define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );

define( 'LOGGED_IN_KEY',    'put your unique phrase here' );

define( 'NONCE_KEY',        'put your unique phrase here' );

define( 'AUTH_SALT',        'put your unique phrase here' );

define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );

define( 'LOGGED_IN_SALT',   'put your unique phrase here' );

define( 'NONCE_SALT',       'put your unique phrase here' );

/**#@-*/



$table_prefix = 'wp_';



define( 'WP_DEBUG', false );



/* That's all, stop editing! Happy publishing. */



if ( ! defined( 'ABSPATH' ) ) {

    define( 'ABSPATH', __DIR__ . '/' );

}



require_once ABSPATH . 'wp-settings.php';