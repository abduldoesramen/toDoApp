import "./event-add-button.styles.css";
import Button from "@mui/material/Button";

const EventAddButton = ({ handleNewEvent }) => {
  return (
    <Button variant="contained" onClick={handleNewEvent}>
      Add To List
    </Button>
  );
};

export default EventAddButton;
