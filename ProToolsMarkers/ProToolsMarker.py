from ProToolsMarkers.Timecode import Timecode

"""
EXAMPLE PRO TOOLS MARKER 1

#   	LOCATION     	TIME REFERENCE    	UNITS    	NAME                             	COMMENTS
1   	01:00:39:12  	2043360           	Samples  	1                                	
========================================================================================================================================================
EXAMPLE PRO TOOLS MARKER 2

#   	LOCATION     	TIME REFERENCE    	UNITS    	NAME                             	TRACK NAME                       	TRACK TYPE   	COMMENTS
1   	01:00:41:20  	2154152           	Samples  	1                                	Cues                             	Ruler                            	
"""

class ProToolsMarker:
    def __init__(self, marker_id: str, location: str, time_reference: str,
                 units: str, name: str, frame_rate: float, comments: str = ""):
        assert marker_id != "" and int(marker_id) >= 0, f"Invalid ProTools Marker ID: {marker_id}"
        assert len(location) == 11 and location[2] == ":" and location[5] == ":" and location[8] == ":", f"Invalid timecode format {location} for ProTools Marker {marker_id}"
        assert int(time_reference) >= 0, f"Invalid location {time_reference} for ProTools Marker {marker_id}"
        assert units == "Samples", f"Unit type {units} unsupported at ProTools Marker {marker_id}"
        assert name != "", f"ProTools Marker name cannot be empty at ProTools Marker {marker_id}"
        assert 0 < frame_rate, "Frame rate must be greater than 0"

        self.marker_id = marker_id
        self.time_reference = time_reference
        self.units = units
        self.name = name
        self.frame_rate = frame_rate

        self.timecode = Timecode.from_frames(location, frame_rate)
        # TODO: rewrite this so it knows how to better handle the hours
        self.timecode.hours = 0
        self.comments = comments
    
    """
    Compare two ProToolsMarker objects to determine if they are equal
    """
    def __eq__(self, other):
        if isinstance(other, ProToolsMarker):
            return (self.marker_id == other.marker_id and
                    self.timecode == other.timecode and
                    self.time_reference == other.time_reference and
                    self.units == other.units and
                    self.name == other.name and
                    self.comments == other.comments)
        
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)