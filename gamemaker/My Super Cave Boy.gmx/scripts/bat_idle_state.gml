/// bat_idle_state()

image_index = spr_bat_idle;

/// Look for the player
// instance exist is to avoid a null pointer if an object doesnt exist
if (instance_exists(Player)) {
    var dis = point_distance(x, y, Player.x, Player.y);
    
    if (dis < sight) {
        state = bat_chase_state;
    }
}
