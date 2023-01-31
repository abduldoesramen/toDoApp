import "./event-translate-button.styles.css";
import Button from "@mui/material/Button";

const EventTranslateButton = ({ handleNewEvent }) => {
  return (
    <Button variant="outlined" onClick={handleNewEvent}>
      Translate 日本語
    </Button>
  );
};

export default EventTranslateButton;
