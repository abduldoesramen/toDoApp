import "./event-container.styles.css";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import DeleteIcon from "@mui/icons-material/Delete";
import IconButton from "@mui/material/IconButton";

const EventContainer = ({ events, handleDelEvent }) => {
  return (
    <div className="event-container" key={events.id}>
      {events.map(({ eventName, id }) => {
        return (
          <div key={id} className="rowEvent">
            <p>{`id=${id}: ${eventName}`}</p>
            <Stack spacing={2} direction="row">
              <IconButton
                aria-label="delete"
                size="medium"
                onClick={() => handleDelEvent(id)}
              >
                <DeleteIcon fontSize="inherit" />
              </IconButton>
            </Stack>
          </div>
        );
      })}
    </div>
  );
};

export default EventContainer;
