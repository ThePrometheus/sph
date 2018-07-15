(function() {
 
  var update_handle_track_pos;

  update_handle_track_pos = function(slider, ui_handle_pos) {
    var handle_track_xoffset, slider_range_inverse_width;
    handle_track_xoffset = -((ui_handle_pos / 100) * slider.clientWidth);
    $(slider).find(".handle-track").css("left", handle_track_xoffset);
    slider_range_inverse_width = (100 - ui_handle_pos) + "%";
    return $(slider).find(".slider-range-inverse").css("width", slider_range_inverse_width);
  };

  // Init slider
  $("#js-slider").slider({
    range: "min",
    max: 100,# Helper function
update_handle_track_pos = (slider, ui_handle_pos) ->
  handle_track_xoffset = -((ui_handle_pos/100) * slider.clientWidth)
  $(slider).find(".handle-track").css("left", handle_track_xoffset)
  
  slider_range_inverse_width = (100 - ui_handle_pos) + "%";
  $(slider).find(".slider-range-inverse").css("width", slider_range_inverse_width)

# Init slider
$("#js-slider").slider
  range: "min"
  max: 100
  value: 50
  create: (event, ui) ->
    slider = $(event.target)
    
    # Append the slider handle with a center dot and it's own track
    slider.find('.ui-slider-handle').append('<span class="dot"><span class="handle-track"></span></span>')
    
    # Append the slider with an inverse range
    slider.prepend('<div class="slider-range-inverse"></div>')
     
    # Set initial dimensions
    slider.find(".handle-track").css("width", event.target.clientWidth)
    
    # Set initial position for tracks
    update_handle_track_pos(event.target, $(this).slider("value"))
    
  slide: (event, ui) ->
    # Update position of tracks
    update_handle_track_pos(event.target, ui.value)
    value: 50,
    create: function(event, ui) {
      var slider;
      slider = $(event.target);
      
      // Append the slider handle with a center dot and it's own track
      slider.find('.ui-slider-handle').append('<span class="dot"><span class="handle-track"></span></span>');
      
      // Append the slider with an inverse range
      slider.prepend('<div class="slider-range-inverse"></div>');
      
      // Set initial dimensions
      slider.find(".handle-track").css("width", event.target.clientWidth);
      
      // Set initial position for tracks
      return update_handle_track_pos(event.target, $(this).slider("value"));
    },
    slide: function(event, ui) {
      // Update position of tracks
      return update_handle_track_pos(event.target, ui.value);
    }
  });

}).call(this);

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiPGFub255bW91cz4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFBQTtBQUFBLE1BQUE7O0VBQ0EsdUJBQUEsR0FBMEIsUUFBQSxDQUFDLE1BQUQsRUFBUyxhQUFULENBQUE7QUFDeEIsUUFBQSxvQkFBQSxFQUFBO0lBQUEsb0JBQUEsR0FBdUIsQ0FBQyxDQUFDLENBQUMsYUFBQSxHQUFjLEdBQWYsQ0FBQSxHQUFzQixNQUFNLENBQUMsV0FBOUI7SUFDeEIsQ0FBQSxDQUFFLE1BQUYsQ0FBUyxDQUFDLElBQVYsQ0FBZSxlQUFmLENBQStCLENBQUMsR0FBaEMsQ0FBb0MsTUFBcEMsRUFBNEMsb0JBQTVDO0lBRUEsMEJBQUEsR0FBNkIsQ0FBQyxHQUFBLEdBQU0sYUFBUCxDQUFBLEdBQXdCO1dBQ3JELENBQUEsQ0FBRSxNQUFGLENBQVMsQ0FBQyxJQUFWLENBQWUsdUJBQWYsQ0FBdUMsQ0FBQyxHQUF4QyxDQUE0QyxPQUE1QyxFQUFxRCwwQkFBckQ7RUFMd0IsRUFEMUI7OztFQVNBLENBQUEsQ0FBRSxZQUFGLENBQWUsQ0FBQyxNQUFoQixDQUNFO0lBQUEsS0FBQSxFQUFPLEtBQVA7SUFDQSxHQUFBLEVBQUssR0FETDtJQUVBLEtBQUEsRUFBTyxFQUZQO0lBR0EsTUFBQSxFQUFRLFFBQUEsQ0FBQyxLQUFELEVBQVEsRUFBUixDQUFBO0FBQ04sVUFBQTtNQUFBLE1BQUEsR0FBUyxDQUFBLENBQUUsS0FBSyxDQUFDLE1BQVIsRUFBVDs7O01BR0EsTUFBTSxDQUFDLElBQVAsQ0FBWSxtQkFBWixDQUFnQyxDQUFDLE1BQWpDLENBQXdDLDZEQUF4QyxFQUhBOzs7TUFNQSxNQUFNLENBQUMsT0FBUCxDQUFlLDBDQUFmLEVBTkE7OztNQVNBLE1BQU0sQ0FBQyxJQUFQLENBQVksZUFBWixDQUE0QixDQUFDLEdBQTdCLENBQWlDLE9BQWpDLEVBQTBDLEtBQUssQ0FBQyxNQUFNLENBQUMsV0FBdkQsRUFUQTs7O2FBWUEsdUJBQUEsQ0FBd0IsS0FBSyxDQUFDLE1BQTlCLEVBQXNDLENBQUEsQ0FBRSxJQUFGLENBQU8sQ0FBQyxNQUFSLENBQWUsT0FBZixDQUF0QztJQWJNLENBSFI7SUFrQkEsS0FBQSxFQUFPLFFBQUEsQ0FBQyxLQUFELEVBQVEsRUFBUixDQUFBLEVBQUE7O2FBRUwsdUJBQUEsQ0FBd0IsS0FBSyxDQUFDLE1BQTlCLEVBQXNDLEVBQUUsQ0FBQyxLQUF6QztJQUZLO0VBbEJQLENBREY7QUFUQSIsInNvdXJjZXNDb250ZW50IjpbIiMgSGVscGVyIGZ1bmN0aW9uXG51cGRhdGVfaGFuZGxlX3RyYWNrX3BvcyA9IChzbGlkZXIsIHVpX2hhbmRsZV9wb3MpIC0+XG4gIGhhbmRsZV90cmFja194b2Zmc2V0ID0gLSgodWlfaGFuZGxlX3Bvcy8xMDApICogc2xpZGVyLmNsaWVudFdpZHRoKVxuICAkKHNsaWRlcikuZmluZChcIi5oYW5kbGUtdHJhY2tcIikuY3NzKFwibGVmdFwiLCBoYW5kbGVfdHJhY2tfeG9mZnNldClcbiAgXG4gIHNsaWRlcl9yYW5nZV9pbnZlcnNlX3dpZHRoID0gKDEwMCAtIHVpX2hhbmRsZV9wb3MpICsgXCIlXCI7XG4gICQoc2xpZGVyKS5maW5kKFwiLnNsaWRlci1yYW5nZS1pbnZlcnNlXCIpLmNzcyhcIndpZHRoXCIsIHNsaWRlcl9yYW5nZV9pbnZlcnNlX3dpZHRoKVxuXG4jIEluaXQgc2xpZGVyXG4kKFwiI2pzLXNsaWRlclwiKS5zbGlkZXJcbiAgcmFuZ2U6IFwibWluXCJcbiAgbWF4OiAxMDBcbiAgdmFsdWU6IDUwXG4gIGNyZWF0ZTogKGV2ZW50LCB1aSkgLT5cbiAgICBzbGlkZXIgPSAkKGV2ZW50LnRhcmdldClcbiAgICBcbiAgICAjIEFwcGVuZCB0aGUgc2xpZGVyIGhhbmRsZSB3aXRoIGEgY2VudGVyIGRvdCBhbmQgaXQncyBvd24gdHJhY2tcbiAgICBzbGlkZXIuZmluZCgnLnVpLXNsaWRlci1oYW5kbGUnKS5hcHBlbmQoJzxzcGFuIGNsYXNzPVwiZG90XCI+PHNwYW4gY2xhc3M9XCJoYW5kbGUtdHJhY2tcIj48L3NwYW4+PC9zcGFuPicpXG4gICAgXG4gICAgIyBBcHBlbmQgdGhlIHNsaWRlciB3aXRoIGFuIGludmVyc2UgcmFuZ2VcbiAgICBzbGlkZXIucHJlcGVuZCgnPGRpdiBjbGFzcz1cInNsaWRlci1yYW5nZS1pbnZlcnNlXCI+PC9kaXY+JylcbiAgICAgXG4gICAgIyBTZXQgaW5pdGlhbCBkaW1lbnNpb25zXG4gICAgc2xpZGVyLmZpbmQoXCIuaGFuZGxlLXRyYWNrXCIpLmNzcyhcIndpZHRoXCIsIGV2ZW50LnRhcmdldC5jbGllbnRXaWR0aClcbiAgICBcbiAgICAjIFNldCBpbml0aWFsIHBvc2l0aW9uIGZvciB0cmFja3NcbiAgICB1cGRhdGVfaGFuZGxlX3RyYWNrX3BvcyhldmVudC50YXJnZXQsICQodGhpcykuc2xpZGVyKFwidmFsdWVcIikpXG4gICAgXG4gIHNsaWRlOiAoZXZlbnQsIHVpKSAtPlxuICAgICMgVXBkYXRlIHBvc2l0aW9uIG9mIHRyYWNrc1xuICAgIHVwZGF0ZV9oYW5kbGVfdHJhY2tfcG9zKGV2ZW50LnRhcmdldCwgdWkudmFsdWUpIl19
//# sourceURL=coffeescript
//# sourceURL=coffeescript
