import React from "react";

export default function SecurityFootnoteCenteredAuthStackWrapper({ text }) {
  return (
    <div style={styles.footnoteWrap}>
      <p style={styles.footnote}>{text}</p>
    </div>
  );
}

const styles = {
  footnoteWrap: {
    display: "flex",
    justifyContent: "center",
  },

  footnote: {
    margin: 0,
    color: "#4A5565",
    fontSize: 14,
    lineHeight: "20px",
    fontWeight: 400,
    letterSpacing: "-0.1504px",
    textAlign: "center",
  },
};