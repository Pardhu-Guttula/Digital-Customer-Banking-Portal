import React from "react";
import { Landmark } from "lucide-react";

export default function BrandMark({ onClick = () => {}, title = "SecureBank Portal" }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={title}
      style={{
        width: 64,
        height: 64,
        borderRadius: 16,
        backgroundColor: "#155DFC",
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        border: 0,
        padding: 0,
        cursor: "pointer",
      }}
    >
      <Landmark size={32} color="#FFFFFF" aria-hidden="true" />
    </button>
  );
}