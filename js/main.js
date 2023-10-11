const BOX_H = 700;
const BOX_W = 200;
const BOX_N = 3;
const Q_N = 35;
const Q_W = 10;
const Q_H = 10;
const Q_R_GAP = 20;
const E_R_O = 4;
const BOX_GAP = 50;
const INIT_X = 10;
const INIT_Y = 30;

function draw() {
  const canvas = document.getElementById("canvas");

  if (canvas.getContext) {
    const ctx = canvas.getContext("2d");
    for (let index = 0; index < BOX_N; index++) {
      drawRect(ctx, index * (BOX_W + BOX_GAP) + INIT_X, INIT_Y, BOX_W, BOX_H);
      for (let j = 0; j < Q_N; j++) {
        for (let k = 0; k < E_R_O; k++) {
          drawRect(
            ctx,
            k * (BOX_W / E_R_O) + (BOX_W + BOX_GAP) * index + +INIT_X,
            INIT_Y + Q_R_GAP * j,
            Q_W,
            Q_H
          );
        }
      }
    }
    // const rectangle = new Path2D();
    // rectangle.rect(300, 30, BOX_W, BOX_H);

    // const circle = new Path2D();
    // circle.arc(100, 35, 25, 0, 2 * Math.PI);

    // ctx.stroke(rectangle);
    // ctx.fill(circle);
  }
}

draw();

function drawRect(ctx, x, y, w, h) {
  console.log(x, y, w, h);
  const rectangle = new Path2D();
  rectangle.rect(x, y, w, h);
  ctx.stroke(rectangle);
}
