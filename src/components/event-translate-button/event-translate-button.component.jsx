import "./event-translate-button.styles.css";
import { useState } from "react";
import Button from "@mui/material/Button";

const EventTranslateButton = ({ handleTranslate, language }) => {
  // Local language in order to render Translate button toggle
  const renderJapanese = "Japanese 日本語";
  const renderEnglish = "English";
  var currLanguage = renderEnglish;
  if (language === "English") {
    currLanguage = renderJapanese;
  } else {
    currLanguage = renderEnglish;
  }

  return (
    <Button variant="outlined" onClick={handleTranslate}>
      Translate to {currLanguage}
    </Button>
  );
};

export default EventTranslateButton;
