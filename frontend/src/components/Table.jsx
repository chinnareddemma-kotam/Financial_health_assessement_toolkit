export default function Table({ data }) {
  if (!data || data.length === 0) return null;

  return (
    <table>
      <thead>
        <tr>
          {Object.keys(data[0]).map((k) => (
            <th key={k}>{k}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, i) => (
          <tr key={i}>
            {Object.values(row).map((v, j) => (
              <td key={j}>{String(v)}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
