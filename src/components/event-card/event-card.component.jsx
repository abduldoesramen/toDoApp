import "./event-card.styles.css";
import { TextField } from "@mui/material/";

const EventCard = ({ value, handleChange }) => {
    return (
        <div className="event-card">
        <TextField
          value={value}
          id="outlined-basic"
          label="Enter event"
          variant="outlined"
          onChange={handleChange}
        />
      </div>
    )
}

export default EventCard;